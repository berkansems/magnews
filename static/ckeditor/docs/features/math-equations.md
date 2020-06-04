---
category: features
menu-title: Math and chemical formulas
---

# Math equations and chemical formulas

<info-box>
	This feature is provided as a commercial solution called MathType delivered by our partner, [Wiris](http://www.wiris.com).
	You can report any issues in the official CKEditor 5 [GitHub repository](https://github.com/ckeditor/ckeditor5/issues). A license can be purchased [here](https://ckeditor.com/contact/).
</info-box>

[MathType](http://www.wiris.com/en/mathtype) is a popular mathematical and science formula editor with classical and handwriting input modes. You can use it to create math equations or chemical formulas right inside the CKEditor 5 content.

MathType is based upon standards like MathML for internal representation and the PNG image format for displaying formulas. It can also handle other formats like LaTeX, Flash, SVG and EPS.

Additionally, MathType offers a special tool designed to help you work with chemical notation. When enabled, ChemType adds a specialized toolbar with the common chemical symbols as well as changes the notation to make it more intuitive to work with chemical formulas.

## Demo

In order to start creating math or chemical formulas in the WYSIWYG editor below, click the MathType or ChemType buttons in the toolbar. This will open the relevant dialog on the screen.

Use the toolbar to write your equation or formula. At any time you can also click the "Go to handwritten mode" button on the right side of the MathType editor to switch to handwriting.

When you are done creating your scientific content, click the "OK" button to insert your formula into CKEditor 5. You can also edit any existing formulas by double-clicking them in your document.

{@snippet features/mathtype}

## Usage

The MathType window is split into two main areas: a [tabbed toolbar](https://docs.wiris.com/en/mathtype/mathtype_web/toolbar) that contains a large number of icons that are useful for creating math equations and chemical formulas, and an editing area where you can see your current formula, the location of the cursor, and the text currently selected (if any).

The following resources can come in handy if you want to become proficient at working with this tool:
* [Using MathType Web](https://docs.wiris.com/en/mathtype/mathtype_web/using_mathtype) covers the basics of creating formulas, using your keyboard, moving the cursor in templates, formatting your content or writing on mobile devices.
* [Introductory tutorials](https://docs.wiris.com/en/mathtype/mathtype_web/intro_tutorials) are intended to get you started using MathType.
* [ChemType](https://docs.wiris.com/en/mathtype/mathtype_web/chemistry) explains the features of the dedicated chemistry toolbar.
* [MathType documentation](https://docs.wiris.com/en/mathtype/mathtype_web/start) is a complete reference to all MathType features and settings.

## Editing modes

MathType lets you choose between two editing modes:
* **Classic input mode** provides options to choose symbols and templates from the MathType or ChemType toolbars and combine them to build the equation.
* **Handwritten input mode** lets you write the equation in your own handwriting. After checking the equation preview to ensure its accuracy, you can insert the equation or switch to classic input for further editing. [Read more here](https://docs.wiris.com/en/mathtype/mathtype_web/handwritten-input).

If you visit a page using MathType with your mobile device, the handwriting interface will appear by default. However, if you visit the same page with a laptop or desktop computer, the classic input will be displayed. The user is always free to change between the two interfaces.

## Installation

To add MathType features to your editor, install the [`@wiris/mathtype-ckeditor5`](https://www.npmjs.com/package/@wiris/mathtype-ckeditor5) package:

```bash
npm install --save @wiris/mathtype-ckeditor5
```

Then add it to your plugin list and the toolbar configuration:

```js
import MathType from '@wiris/mathtype-ckeditor5';

ClassicEditor
	.create( document.querySelector( '#editor' ), {
		plugins: [ MathType, ... ],
		toolbar: [ 'MathType', 'ChemType', ... ]
	} )
	.then( ... )
	.catch( ... );
```

<info-box info>
	Read more about {@link builds/guides/integration/installing-plugins installing plugins}.
</info-box>
