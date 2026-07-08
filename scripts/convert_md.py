'''Convert Obsidian markdown to Jupyter Book format.'''
import re
import shutil
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
VAULT = Path(r'C:\Users\lakj\Documents\vault_1\BSSDH')
DATA = Path(r'C:\Users\lakj\Documents\GitHub\BSSDH2026\data\Makslu kritika\bssdh openrefine and orange final')

# URL for large image zip (hosted via GitHub Release, not gh-pages)
RELEASE_ZIP_URL = 'https://github.com/lrskjr/BSSDH2026-book/releases/download/workshop-data/daells-warehouse-categories.zip'

DOC_MAP = {
    'OpenRefine_en': 'openrefine.md',
    'Orange_en': 'orange.md',
}

SECTION_SLUGS = {
    'When would I use OpenRefine?': 'when-would-i-use-openrefine',
    'How do I get data into the program?': 'how-do-i-get-data-into-the-program',
    'Split into several columns': 'split-into-several-columns',
    'Transform and GREL': 'transform-and-grel',
    'Task: Split host_info into three columns': 'task-split-host_info-into-three-columns',
    'Join columns': 'join-columns',
    'Task: Clean and rename host_name 1–3': 'task-clean-and-rename-host_name-1-3',
    'Transform and advanced GREL solutions': 'transform-and-advanced-grel-solutions',
    'Text facets and clusters': 'text-facets-and-clusters',
    'Task: Clean the author and topic columns with clustering': 'task-clean-the-author-and-topic-columns-with-clustering',
    'How do I export the project to a new file?': 'how-do-i-export-the-project-to-a-new-file',
    'Resource': 'resource',
    'When would I use Orange?': 'when-would-i-use-orange',
    'Documentation': 'documentation',
    'Interactivity': 'interactivity',
    'Add-ons': 'add-ons',
    'Import CSV files and build a workflow to analyse the landscape of language': 'import-csv-files-and-build-a-workflow-to-analyse-the-landscape-of-language',
    'Merge two datasets and analyse data distribution': 'merge-two-datasets-and-analyse-data-distribution',
    'Select Rows and Edit Domain and analyse how authors write': 'select-rows-and-edit-domain-and-analyse-how-authors-write',
    'Geocoding of geographical data in the metadata': 'geocoding-of-geographical-data-in-the-metadata',
    'Corpus linguistic methods on titles and sub titles': 'corpus-linguistic-methods-on-titles-and-sub-titles',
    'And now to something different - Image classification': 'and-now-to-something-different-image-classification',
    'And now to something different — Image classification': 'and-now-to-something-different-image-classification',
}

# original filename -> URL-safe filename (filled by copy_assets)
IMAGE_MAP: dict[str, str] = {}
OWS_MAP: dict[str, str] = {}


def slugify_filename(name: str) -> str:
    path = Path(name)
    stem = path.stem.lower()
    stem = stem.replace('—', '-').replace('–', '-')
    stem = re.sub(r'[^a-z0-9]+', '-', stem)
    stem = re.sub(r'-+', '-', stem).strip('-')
    return f'{stem}{path.suffix.lower()}'


def slugify_heading(text: str) -> str:
    if text in SECTION_SLUGS:
        return SECTION_SLUGS[text]
    s = text.lower().strip()
    s = s.replace('—', '-').replace('–', '-')
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s.strip('-')


def resolve_image_name(name: str) -> str:
    if name.startswith('assets/'):
        name = name[len('assets/'):]
    return IMAGE_MAP.get(name, slugify_filename(name))


def convert_wikilink(match: re.Match, prefix: str) -> str:
    inner = match.group(1)
    if '|' in inner:
        label, target = inner.split('|', 1)
    else:
        target = inner
        label = None

    if '#' in target:
        doc, section = target.split('#', 1)
    else:
        doc, section = target, None

    if doc in DOC_MAP:
        href = f'{prefix}{DOC_MAP[doc]}'
        if section:
            href += f'#{slugify_heading(section)}'
        text = label or section or doc.replace('_en', '')
        return f'[{text}]({href})'

    return match.group(0)


def convert_images(text: str, image_prefix: str) -> str:
    def repl_wiki(m: re.Match) -> str:
        safe = resolve_image_name(m.group(1))
        return f'![screenshot]({image_prefix}{safe})'

    text = re.sub(r'!\[\[([^\]]+)\]\]', repl_wiki, text)

    # fix already-converted markdown images that still use spaces in paths
    def repl_md(m: re.Match) -> str:
        alt, path = m.group(1), m.group(2)
        filename = Path(path).name
        safe = IMAGE_MAP.get(filename, slugify_filename(filename))
        prefix = path[: -len(filename)] if path.endswith(filename) else image_prefix
        return f'![{alt}]({prefix}{safe})'

    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl_md, text)


def convert_content(text: str, link_prefix: str, image_prefix: str) -> str:
    text = text.lstrip('\ufeff')
    text = convert_images(text, image_prefix)
    text = re.sub(
        r'\[\[([^\]]+)\]\]',
        lambda m: convert_wikilink(m, link_prefix),
        text,
    )
    return text


def setup_dirs() -> None:
    for rel in [
        'workshops',
        'instructor',
        '_static/images',
        '_static/files/data',
        '_static/files/orange',
        '.github/workflows',
    ]:
        (BOOK / rel).mkdir(parents=True, exist_ok=True)


def copy_assets() -> None:
    src_assets = VAULT / 'assets'
    dst = BOOK / '_static' / 'images'
    IMAGE_MAP.clear()

    for old in dst.iterdir():
        if old.is_file():
            old.unlink()

    for f in src_assets.iterdir():
        if f.is_file():
            safe_name = slugify_filename(f.name)
            IMAGE_MAP[f.name] = safe_name
            shutil.copy2(f, dst / safe_name)


def copy_data_files() -> None:
    data_dst = BOOK / '_static' / 'files' / 'data'
    orange_dst = BOOK / '_static' / 'files' / 'orange'
    OWS_MAP.clear()

    data_files = [
        'metadata_bssdh.csv',
        'record_id_udc_number_udc_label_en.csv',
        'geodata.csv',
        'stopwords-lv.txt',
        'geomap.html',
    ]
    for name in data_files:
        shutil.copy2(DATA / name, data_dst / name)

    for old in orange_dst.iterdir():
        if old.is_file():
            old.unlink()

    for f in DATA.glob('*.ows'):
        safe_name = slugify_filename(f.name)
        OWS_MAP[f.name] = safe_name
        shutil.copy2(f, orange_dst / safe_name)


def dl_link(path: str, label: str, download: bool = False) -> str:
    '''HTML link — avoids MyST mis-parsing markdown paths as xrefs.'''
    if download:
        return f'<a href="{path}" download="{label}">{label}</a>'
    return f'<a href="{path}">{label}</a>'


def strip_openrefine_logo(text: str) -> str:
    text = re.sub(r'^!\[\[assets/openrefine_logo\.svg\]\]\s*\n+', '', text)
    text = re.sub(r'^!\[[^\]]*\]\([^)]*openrefine-logo\.svg\)\s*\n+', '', text, count=1)
    return text


def write_converted(
    src_name: str,
    dst_rel: str,
    link_prefix: str,
    image_prefix: str,
    title: str | None = None,
) -> None:
    src = VAULT / src_name
    text = src.read_text(encoding='utf-8-sig')
    if src_name == 'OpenRefine_en.md':
        text = strip_openrefine_logo(text)
    text = convert_content(text, link_prefix, image_prefix)
    if title:
        text = f'# {title}\n\n' + text
    (BOOK / dst_rel).write_text(text, encoding='utf-8', newline='\n')


def write_downloads() -> None:
    lines = [
        '# Downloads',
        '',
        'All workshop files are available for direct download below.',
        '',
        '## Data files',
        '',
        '| File | Description |',
        '|------|-------------|',
        f'| {dl_link("_static/files/data/metadata_bssdh.csv", "metadata_bssdh.csv", download=True)} | Main workshop dataset (cleaned bibliographic metadata) |',
        f'| {dl_link("_static/files/data/record_id_udc_number_udc_label_en.csv", "record_id_udc_number_udc_label_en.csv", download=True)} | UDC numbers with English labels (for Merge Data in Orange) |',
        f'| {dl_link("_static/files/data/geodata.csv", "geodata.csv", download=True)} | Geographical data for geocoding workflows |',
        f'| {dl_link("_static/files/data/stopwords-lv.txt", "stopwords-lv.txt", download=True)} | Latvian stopwords for text mining |',
        f'| {dl_link("_static/files/data/geomap.html", "geomap.html")} | Exported geo map (reference) |',
        '',
        '## Image dataset (Orange workshop 6)',
        '',
        'Pages from historical department store catalogues for the Image Analytics workflow.',
        'Unzip after download and import the folder in Orange with **Import Images**.',
        '',
        '| File | Description |',
        '|------|-------------|',
        f'| <a href="{RELEASE_ZIP_URL}" download="daells-warehouse-categories.zip">daells-warehouse-categories.zip</a> | Image folder for workflow 6 — Image classification (~184 MB) |',
        '',
        '## Orange workflows (.ows)',
        '',
        'Open these files in Orange (File -> Open) after downloading.',
        '',
        '| Workflow | File |',
        '|----------|------|',
    ]

    ows_rows = [
        ('1 — Language landscape', '1 language landscape.ows'),
        ('2 — UDC labels', '2 udc_labels.ows'),
        ('3 — Authors', '3 authors.ows'),
        ('4 — Geodata', '4 geodata.ows'),
        ('5 — Corpus (Latvian titles)', '5 corpus linguistic tools on latvian titles.ows'),
        ('6 — Image classification', '6 Images classification.ows'),
    ]
    for label, original in ows_rows:
        safe = OWS_MAP.get(original, slugify_filename(original))
        lines.append(
            f'| {label} | {dl_link(f"_static/files/orange/{safe}", safe, download=True)} |'
        )

    lines.extend([
        '',
        '## Workflow diagrams (.svg)',
        '',
        'These images are also embedded in the [Orange workshop guide](workshops/orange.md).',
        '',
    ])

    svg_keys = [
        '1 language landscape.svg',
        '2 udc_labels.svg',
        '3 authors 3.svg',
        '4 geodata.svg',
        '5 corpus linguistic tools on latvian titles.svg',
        '6 Images classification.svg',
    ]
    for key in svg_keys:
        safe = IMAGE_MAP.get(key, slugify_filename(key))
        lines.append(f'- {dl_link(f"_static/images/{safe}", key)}')

    (BOOK / 'downloads.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> None:
    setup_dirs()
    copy_assets()
    copy_data_files()

    write_converted(
        'OpenRefine_en.md',
        'workshops/openrefine.md',
        link_prefix='',
        image_prefix='../_static/images/',
        title='Data cleaning with OpenRefine',
    )
    write_converted(
        'Orange_en.md',
        'workshops/orange.md',
        link_prefix='',
        image_prefix='../_static/images/',
        title='Analysis and Visualization with Orange Data Mining',
    )
    write_converted(
        'OpenRefine_Sekvensplan_en.md',
        'instructor/openrefine-sequence.md',
        link_prefix='../workshops/',
        image_prefix='../_static/images/',
    )
    write_converted(
        'Orange Sekvensplan_en.md',
        'instructor/orange-sequence.md',
        link_prefix='../workshops/',
        image_prefix='../_static/images/',
    )
    write_downloads()
    print('Conversion complete.')
    print(f'Images renamed: {len(IMAGE_MAP)}')


if __name__ == '__main__':
    main()
