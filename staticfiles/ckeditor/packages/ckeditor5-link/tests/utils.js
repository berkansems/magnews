/**
 * @license Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or https://ckeditor.com/legal/ckeditor-oss-license
 */

import ViewDocument from '@ckeditor/ckeditor5-engine/src/view/document';
import ViewDowncastWriter from '@ckeditor/ckeditor5-engine/src/view/downcastwriter';
import AttributeElement from '@ckeditor/ckeditor5-engine/src/view/attributeelement';
import ContainerElement from '@ckeditor/ckeditor5-engine/src/view/containerelement';
import Text from '@ckeditor/ckeditor5-engine/src/view/text';

import { createLinkElement, isLinkElement, ensureSafeUrl, normalizeDecorators } from '../src/utils';

describe( 'utils', () => {
	describe( 'isLinkElement()', () => {
		it( 'should return true for elements created by createLinkElement', () => {
			const element = createLinkElement( 'http://ckeditor.com', new ViewDowncastWriter( new ViewDocument() ) );

			expect( isLinkElement( element ) ).to.be.true;
		} );

		it( 'should return false for other AttributeElements', () => {
			expect( isLinkElement( new AttributeElement( 'a' ) ) ).to.be.false;
		} );

		it( 'should return false for ContainerElements', () => {
			expect( isLinkElement( new ContainerElement( 'p' ) ) ).to.be.false;
		} );

		it( 'should return false for text nodes', () => {
			expect( isLinkElement( new Text( 'foo' ) ) ).to.be.false;
		} );
	} );

	describe( 'createLinkElement()', () => {
		it( 'should create link AttributeElement', () => {
			const element = createLinkElement( 'http://cksource.com', new ViewDowncastWriter( new ViewDocument() ) );

			expect( isLinkElement( element ) ).to.be.true;
			expect( element.priority ).to.equal( 5 );
			expect( element.getAttribute( 'href' ) ).to.equal( 'http://cksource.com' );
			expect( element.name ).to.equal( 'a' );
		} );
	} );

	describe( 'ensureSafeUrl()', () => {
		it( 'returns the same absolute http URL', () => {
			const url = 'http://xx.yy/zz#foo';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same absolute https URL', () => {
			const url = 'https://xx.yy/zz';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same absolute ftp URL', () => {
			const url = 'ftp://xx.yy/zz';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same absolute ftps URL', () => {
			const url = 'ftps://xx.yy/zz';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same absolute mailto URL', () => {
			const url = 'mailto://foo@bar.com';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same relative URL (starting with a dot)', () => {
			const url = './xx/yyy';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same relative URL (starting with two dots)', () => {
			const url = '../../xx/yyy';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same relative URL (starting with a slash)', () => {
			const url = '/xx/yyy';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same relative URL (starting with a backslash)', () => {
			const url = '\\xx\\yyy';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same relative URL (starting with a letter)', () => {
			const url = 'xx/yyy';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same URL even if it contains whitespaces', () => {
			const url = '  ./xx/ yyy\t';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'returns the same URL even if it contains non ASCII characters', () => {
			const url = 'https://kłącze.yy/źdźbło';

			expect( ensureSafeUrl( url ) ).to.equal( url );
		} );

		it( 'accepts non string values', () => {
			expect( ensureSafeUrl( undefined ) ).to.equal( 'undefined' );
			expect( ensureSafeUrl( null ) ).to.equal( 'null' );
		} );

		it( 'returns safe URL when a malicious URL starts with javascript:', () => {
			const url = 'javascript:alert(1)';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );

		it( 'returns safe URL when a malicious URL starts with an unknown protocol', () => {
			const url = 'foo:alert(1)';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );

		it( 'returns safe URL when a malicious URL contains spaces', () => {
			const url = 'java\u0000script:\talert(1)';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );

		it( 'returns safe URL when a malicious URL contains spaces (2)', () => {
			const url = '\u0000 javascript:alert(1)';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );

		it( 'returns safe URL when a malicious URL contains a safe part', () => {
			const url = 'javascript:alert(1)\nhttp://xxx';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );

		it( 'returns safe URL when a malicious URL contains a safe part (2)', () => {
			const url = 'javascript:alert(1);http://xxx';

			expect( ensureSafeUrl( url ) ).to.equal( '#' );
		} );
	} );

	describe( 'normalizeDecorators()', () => {
		it( 'should transform an entry object to a normalized array', () => {
			const callback = () => {};
			const entryObject = {
				foo: {
					mode: 'manual',
					label: 'Foo',
					attributes: {
						foo: 'foo'
					}
				},
				bar: {
					mode: 'automatic',
					callback,
					attributes: {
						bar: 'bar'
					}
				},
				baz: {
					mode: 'manual',
					label: 'Baz label',
					attributes: {
						target: '_blank',
						rel: 'noopener noreferrer'
					}
				}
			};

			expect( normalizeDecorators( entryObject ) ).to.deep.equal( [
				{
					id: 'linkFoo',
					mode: 'manual',
					label: 'Foo',
					attributes: {
						foo: 'foo'
					}
				},
				{
					id: 'linkBar',
					mode: 'automatic',
					callback,
					attributes: {
						bar: 'bar'
					}
				},
				{
					id: 'linkBaz',
					mode: 'manual',
					label: 'Baz label',
					attributes: {
						target: '_blank',
						rel: 'noopener noreferrer'
					}
				}
			] );
		} );
	} );
} );
