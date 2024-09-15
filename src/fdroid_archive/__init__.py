import argparse
import subprocess
import ruamel.yaml

def get_pkgs():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('pkg', help='Package to archive', nargs='+')
    args = arg_parser.parse_args()
    return args.pkg

def main():
    pkgs = get_pkgs()

    for pkg in pkgs:
        with open(f'metadata/{pkg}.yml') as f:
            metadata = ruamel.yaml.YAML().load(f)

        metadata['ArchivePolicy'] = 1
        metadata['AutoUpdateMode'] = 'None'
        metadata['UpdateCheckMode'] = 'None'

        with open(f'metadata/{pkg}.yml', 'w') as f:
            ruamel.yaml.YAML().dump(metadata, f)



        subprocess.run(f'fdroid rewritemeta {pkg}', shell=True)
        print(f'Archived metadata/{pkg}.yml')

if __name__ == '__main__':
    main()