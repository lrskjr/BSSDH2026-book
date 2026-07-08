'''Convert Obsidian markdown to Jupyter Book format.'''
import re
import shutil
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
VAULT = Path(r'C:\Users\lakj\Documents\vault_1\BSSDH')
DATA = Path(r'C:\Users\lakj\Documents\GitHub\BSSDH2026\data\Makslu kritika\bssdh openrefine and orange final')

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


def slugify_heading(text: str) -> str:
    if text in SECTION_SLUGS:
        return SECTION_SLUGS[text]
    s = text.lower().strip()
    s = s.replace('—', '-').replace('–', '-')
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s.strip('-')


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
    def repl(m: re.Match) -> str:
        path = m.group(1)
        if path.startswith('assets/'):
            path = path[len('assets/'):]
        return f'![{path}]({image_prefix}{path})'
    return re.sub(r'!\[\[([^\]]+)\]\]', repl, text)


def convert_content(text: str, link_prefix: str, image_prefix: str) -> str:
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
    for f in src_assets.iterdir():
        if f.is_file():
            shutil.copy2(f, dst / f.name)


def copy_data_files() -> None:
    data_dst = BOOK / '_static' / 'files' / 'data'
    orange_dst = BOOK / '_static' / 'files' / 'orange'

    data_files = [
        'metadata_bssdh.csv',
        'record_id_udc_number_udc_label_en.csv',
        'geodata.csv',
        'stopwords-lv.txt',
        'geomap.html',
    ]
    for name in data_files:
        shutil.copy2(DATA / name, data_dst / name)

    for f in DATA.glob('*.ows'):
        shutil.copy2(f, orange_dst / f.name)


def write_converted(src_name: str, dst_rel: str, link_prefix: str, image_prefix: str, title: str | None = None) -> None:
    src = VAULT / src_name
    text = src.read_text(encoding='utf-8')
    text = convert_content(text, link_prefix, image_prefix)
    if title:
        text = f'# {title}\n\n' + text
    (BOOK / dst_rel).write_text(text, encoding='utf-8', newline='\n')


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
    print('Conversion complete.')


if __name__ == '__main__':
    main()
