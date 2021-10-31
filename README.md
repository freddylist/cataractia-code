# Cataractia Code

Microsoft's [Cascadia Code](https://github.com/microsoft/cascadia-code) font
customized to my liking. Also includes some simple batch patch and bake scripts to batch
patch glyphs and bake font features into fonts!

**These are my first shell scripts so they are probably garbage!**

## Customizations

The fonts in [`./final`](https://github.com/freddylist/cataractia-code/tree/main/final) have been patched to include the complete [nerd
font](https://www.nerdfonts.com/) icons set. The [stylistic
sets](https://github.com/microsoft/cascadia-code#font-features) `calt` + `ss01`
(for cursive italics), `ss02` (alternate not-equal), `ss19`/`zero` (slashed
zero), and `ss20` (graphical control characters) have also been baked into the
fonts.

## Download

Download Cataractia Code from the repository's
[releases](https://github.com/freddylist/cataractia-code/releases) page!

## Customize yourself

**Instructions for Windows users, sorry Linux and OS X users, you will have to
figure it out on your own (do make a pull request if you would like to add
instructions for your operating system)**

You might believe that I must be blind to think these customizations look good,
(hence the name Cataractia Code, haha), so here are the instructions to patch your own
fonts:

### Requirements

* [**Python 3**](https://www.python.org/) + pip
  * [**Opentype Feature
    Freezer**](https://github.com/twardoch/fonttools-opentype-feature-freezer)
    `pip install --upgrade opentype-feature-freezer`
* [**Font Forge**](https://fontforge.org/) (if you want nerd font icons)
  * Make sure you add the Font Forge bin to your path.

### Instructions

1. Open git bash
7. `cd` into whatever directory you have all of your git repositories
2. Clone this repository `git clone
   https://github.com/freddylist/cataractia-code.git`
4. `cd` into the repository
6. Remove the fonts in `./patched`, `./frozen`, and `./final`
    * Remove the fonts in `./original` as well if you don't want to customize
      Cascadia Code.
25. Add fonts you would like to customize in `./original`
    * Make sure the fonts are static (not variable), I don't think FontForge likes variable fonts. If you're just freezing features
      though, then variable fonts should be fine.
3. Edit the scripts in `./scripts` to do what you would like them to do
    * For example, in `bake.sh` and `patch.sh`, edit `ARGS` to pass in whatever
      arguments you want to [feature
      freezer](https://github.com/ryanoasis/nerd-fonts#font-patcher) and [nerd
      font
      patcher](https://github.com/twardoch/fonttools-opentype-feature-freezer#documentation)
      (read what arguments you can pass on their pages). In `rename.sh`, edit
      `REPLACEMENTS` to change what font names get replaced in the font (format:
      `name/replacement,name/replacement,...`)
72. Run some scripts
    * Example: `./scripts/bake.sh`
    * I recommend running `bake.sh` before `patch.sh` (for no particular reason,
      I just have a feeling it works better like that) and running `rename.sh` last.
193948. Profit!

## Credits

* [microsoft/cascadia-code](https://github.com/microsoft/cascadia-code)
* [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts) [font
  patcher](https://github.com/ryanoasis/nerd-fonts#font-patcher)
* [twardoch/fonttools-opentype-feature-freezer](https://github.com/twardoch/fonttools-opentype-feature-freezer)