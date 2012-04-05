from __future__ import print_function
import numpy as np
import matplotlib
from matplotlib.testing.decorators import image_comparison, knownfailureif, cleanup
import matplotlib.pyplot as plt
import warnings
from nose.tools import with_setup


@image_comparison(baseline_images=['font_styles'])
def test_font_styles():
    from matplotlib import _get_data_path
    data_path = _get_data_path()

    def find_matplotlib_font(**kw):
        prop = FontProperties(**kw)
        path = findfont(prop, directory=data_path)
        return FontProperties(fname=path)

    from matplotlib.font_manager import FontProperties, findfont
    warnings.filterwarnings('ignore','findfont: Font family \[\'Foo\'\] not found. Falling back to .',UserWarning,module='matplotlib.font_manager')
    fig = plt.figure()
    ax = plt.subplot( 1, 1, 1 )

    normalFont = find_matplotlib_font( family = "sans-serif",
                                       style = "normal",
                                       variant = "normal",
                                       size = 14,
                                       )
    ax.annotate( "Normal Font", (0.1, 0.1), xycoords='axes fraction',
                  fontproperties = normalFont )

    boldFont = find_matplotlib_font( family = "Foo",
                                     style = "normal",
                                     variant = "normal",
                                     weight = "bold",
                                     stretch = 500,
                                     size = 14,
                                     )
    ax.annotate( "Bold Font", (0.1, 0.2), xycoords='axes fraction',
                  fontproperties = boldFont )

    boldItemFont = find_matplotlib_font( family = "sans serif",
                                         style = "italic",
                                         variant = "normal",
                                         weight = 750,
                                         stretch = 500,
                                         size = 14,
                                         )
    ax.annotate( "Bold Italic Font", (0.1, 0.3), xycoords='axes fraction',
                  fontproperties = boldItemFont )

    lightFont = find_matplotlib_font( family = "sans-serif",
                                      style = "normal",
                                      variant = "normal",
                                      weight = 200,
                                      stretch = 500,
                                      size = 14,
                                      )
    ax.annotate( "Light Font", (0.1, 0.4), xycoords='axes fraction',
                  fontproperties = lightFont )

    condensedFont = find_matplotlib_font( family = "sans-serif",
                                          style = "normal",
                                          variant = "normal",
                                          weight = 500,
                                          stretch = 100,
                                          size = 14,
                                          )
    ax.annotate( "Condensed Font", (0.1, 0.5), xycoords='axes fraction',
                  fontproperties = condensedFont )

    ax.set_xticks([])
    ax.set_yticks([])

@image_comparison(baseline_images=['image'], extensions=['png'])
def test_default_rcparam():
	fig = plt.figure()
	fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

	ax = fig.add_subplot(111)
	fig.subplots_adjust(top=0.85)
	ax.set_title('axes title')

	ax.set_xlabel('xlabel')
	ax.set_ylabel('ylabel')

	ax.text(3, 8, 'boxed italics text in data coords', style='italic',
		)

	ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

	ax.text(3, 2, unicode('unicode: Institut f\374r Festk\366rperphysik', 'latin-1'))

	ax.text(0.95, 0.01, 'colored text in axes coords',
		verticalalignment='bottom', horizontalalignment='right',
		transform=ax.transAxes,
		color='green', fontsize=15)


	ax.plot([2], [1], 'o')
	ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
		    arrowprops=dict(facecolor='black', shrink=0.05))

	ax.axis([0, 10, 0, 10])

	fig.savefig('image.png')

@image_comparison(baseline_images=['multiline'])
def test_multiline():
    fig = plt.figure()
    ax = plt.subplot( 1, 1, 1 )
    ax.set_title("multiline\ntext alignment")

    ax.set_xticks([])
    ax.set_yticks([])

@image_comparison(baseline_images=['antialiased'], extensions=['png'],
                  freetype_version=("2.4.5", "2.4.6"))
def test_antialiasing():
    matplotlib.rcParams['text.antialiased'] = True

    fig = plt.figure(figsize=(5.25, 0.75))
    fig.text(0.5, 0.75, "antialiased", horizontalalignment='center', verticalalignment='center')
    fig.text(0.5, 0.25, "$\sqrt{x}$", horizontalalignment='center', verticalalignment='center')
    # NOTE: We don't need to restore the rcParams here, because the
    # test cleanup will do it for us.  In fact, if we do it here, it
    # will turn antialiasing back off before the images are actually
    # rendered.
