# MultiFarms

MultiFarms is a mod for Stardew Valley that allows you to manage multiple farms, you can choose between 4, 8, 12 or 16 Farms

## Requirements

To compile and use the mod, you need to have installed:

* [Python](https://www.python.org/)
* The `stardewmodpy` library (installable via pip):

```bash
pip install stardewmodpy
```

## Setting up the environment

1. Download the **Content Patcher** mod and place the **.zip** file inside the `frameworks/` folder.

   > The file must be in **.zip** format, not extracted.

2. If you want to test the mod with cheats or other mods, you can place the desired **.zip** files inside the `dependences/` folder.

## Compiling the mod

To compile the mod, follow these steps:

1. Download the MultiFarms repository.
2. Run the command:

```bash
sdvpy run
```

* This command **compiles the mod and launches the game directly**.

If you only want to generate the compiled mod without running the game, use:

```bash
sdvpy run MultiFarms
```

* This will generate the `.zip` file of the mod inside `MultiFarms/dist`.

## Folder structure

* `frameworks/` → Contains the Content Patcher (zip).
* `dependences/` → Place additional mod zips for testing.
* `MultiFarms/dist/` → Folder where the compiled mod is generated.


## License

MIT License

Copyright (c) 2025 by alichan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

