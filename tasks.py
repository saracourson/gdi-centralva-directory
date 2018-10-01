import json
from pathlib import Path
import webbrowser

from mako.template import Template
from invoke import task
from invocations.watch import watch as watch_task

HERE = Path('.')
BUILD = HERE / 'built'
REPO = 'GirlDevelopItCentralVA/gdi-centralva-directory'

def collect_json(source_dir):
    ret = []
    source_path = Path(source_dir)
    for file_path in source_path.glob('*.json'):
        with file_path.open() as fp:
            ret.append(json.load(fp))
    return sorted(ret, key=lambda each: each['name'])

def render_site():
    index = Template(filename=str(HERE / 'index.mako'))
    return index.render(
        repo=REPO,
        people=collect_json(str(HERE / 'people')),
    )

@task
def build(ctx, browse=False):
    try:
        BUILD.mkdir()
    except FileExistsError:
        pass
    index_path = BUILD / 'index.html'
    with index_path.open('w') as fp:
        fp.write(render_site())
    print('Finished building site.')
    if browse:
        webbrowser.open_new_tab(str(index_path))


@task
def watch(ctx, browse=False):
    if browse:
        build(ctx, browse=True)
    print('Watching for changes...')
    watch_task(
        ctx, build, ['\.'], ['.*/\..*\.swp', './built/*']
    )
