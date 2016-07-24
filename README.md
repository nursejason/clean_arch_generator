# clean_arch_generator

This program is responsible for automatic template generation for Clean Architecture projects.

#### Features
- Create a base directory and lib folders based on some params.
  - **Flag to insert into existing repo at X dir**
  - Give a base repo dir (`~/changelog-api-auth/`)
  - Give a parent project name (`changelog`)
  - Give a specific project name (`auth`)
  - The above will generate:

```
    - ~/changelog-api-auth/
      - /lib/
        - __init__.py
        - /changelog/
          - __init__.py
          - /auth/
            - __init__.py
            - adapters.py
            - application.py
            - domain.py
            - handlers.py
            - main.py

```
### Optional
- Create **empty** adapter classes for all given adapter args.
  - **Automatically generate code for X handlers that are predefined.**

- Create **empty** domain classes for all given domain args.

- Create **empty** handler classes for all given handler args.

- Add base Flask setup if flag is passed.

#### Future

#### Args

```bash
python2.7 bin/clean_gen.py \\
    --base_dir ~/changelog-api-auth \\
    --parent_project changelog \\
    --specific_project auth \\
    --adapter mysql,couchbase \\
    --domain user \\
    --handler user_handler \\
    -new
    -flask
```
