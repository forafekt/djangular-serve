#!/usr/bin/python3
"""""
DJANGULAR SERVE MAIN
IN DEVELOPMENT
"""""
import argparse

try:
    from djangular_serve.management.objects import AngularBuild, ng_deploy, move_js, move_css, move_img, move_all, \
        make_directory
    from djangular_serve.management.exceptions import ArgDoesNotExist
except (ModuleNotFoundError, ValueError):
    from .management.objects import AngularBuild
    from .management.exceptions import ArgDoesNotExist


def main():
    """""
    DJANGULAR SERVE args
    """""
    parser = argparse.ArgumentParser(
        prog='serve',
        description='Automate your Django / Angular projects'
                    ' with DJANGULAR-SERVE.'
    )

    parser.add_argument(
        '-s',
        '--serve',
        type=str,
        help='Build Angular to Django static.'
    )

    parser.add_argument(
        '-mv',
        '--move',
        type=str,
        help='Move files to respective directories.'
    )

    parser.add_argument(
        '-mk',
        '--mkdir',
        type=str,
        help='Make a new sub directory in your static files folder.'
    )
    args = parser.parse_args()

    """""
    Serve
    """""
    serve = args.serve
    move = args.move
    mkdir = args.mkdir

    #    if not os.path.isfile(p):
    #        print('The specified source file does not exist')
    #        sys.exit()

    arg_is_none = ArgDoesNotExist("Argument does not exist. Did you mean...\n"
                                  "serve -s static\n"
                                  "serve -mv js, css, img or all\n"
                                  "serve -mk <any-dir>\n")
    if not args:
        raise arg_is_none

    try:

        """""
        Serve
        """""
        if serve:
            if serve == "static":
                ng_deploy()
            else:
                pass

        """""
        Move
        """""
        if move:
            if move == "js":
                move_js()
            else:
                pass

        if move:
            if move == "css":
                move_css()
            else:
                pass

        if move:
            if move == "img":
                move_img()
            else:
                pass

        if move:
            if move == 'all':
                move_all()
        else:
            pass

        if mkdir:
            make_directory(mkdir)
        else:
            pass

    except KeyboardInterrupt:
        print("\n => You have force cancelled the session.\n")


if __name__ == '__main__':
    main()
