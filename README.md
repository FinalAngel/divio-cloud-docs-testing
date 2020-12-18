# PDF GENERATION

- Make sure latexmk is installed

Run the build in one terminal:

```
make latex
```

Run latexmk in the another terminal window:

```
cd _build/latex
latexmk -pdf -pvc -f
```
