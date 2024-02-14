
## Insert Template in your Project

```shell
git checkout -b translations-templete
git checkout translations-templete
git config pull.rebase false
git pull https://github.com/DRincs-Productions/renpy-translations-templete.git tool-only --allow-unrelated-histories
git submodule update --init --recursive

```

At the end make a merge inside the arm of the project.

### Fix Common
```regex
    # renpy/common/(.*)
    old "###########"
    new "(.*)"
```

```regex
    # # renpy/common/(.*)
    # old "###########"
    # new "(.*)"
```
