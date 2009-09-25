__test__ = {'NAVIGATION_TESTS': """

Make sure breadcrumb navigation renders correctly.

    >>> from django.core import management
    >>> management.call_command('loaddata', 'initial_data.xml', verbosity=0)
    >>> import os.path
    >>> from pages import settings
    >>> from pages.templatetags.navigation import NavigationNode
    >>> from pages.models import Page
    >>> from django.template.context import Context
    >>> NavigationNode()
    Traceback (most recent call last):
    ...
    TypeError: __init__() takes at least 2 arguments (1 given)
    >>> nn = NavigationNode(mode="breadcrumb", xml_file=os.path.join(settings.CURDIR, "fixtures", "navigation.xml"))
    >>> c = Context(dict(nav_node=Page.objects.get(id=3)))
    >>> nn.render(c)
    '<div id="breadcrumb"><ol><li class="homepagelistitem" id="breadcrumb_home"><a class="homepage" href="/1/home/">Home</a></li><li class="sectionlistitem currentsectionlistitem" id="breadcrumb_vestibulum-leo"><a class="section currentsection" href="/2/vestibulum-leo/">Vestibulum Leo</a></li><li class="currentpagelistitem" id="breadcrumb_fermentum-viverra"><a class="currentpage" href="/3/fermentum-viverra/">Fermentum Viverra</a></li></ol></div>'
    >>> c = Context(dict(nav_node=Page.objects.get(id=2)))
    >>> nn.render(c)
    '<div id="breadcrumb"><ol><li class="homepagelistitem" id="breadcrumb_home"><a class="homepage" href="/1/home/">Home</a></li><li class="sectionlistitem currentsectionlistitem currentpagelistitem" id="breadcrumb_vestibulum-leo"><a class="section currentsection currentpage" href="/2/vestibulum-leo/">Vestibulum Leo</a></li></ol></div>'
    >>> c = Context(dict(nav_node=Page.objects.get(id=1)))
    >>> nn.render(c)
    '<div id="breadcrumb"><ol><li class="homepagelistitem currentpagelistitem" id="breadcrumb_home"><a class="homepage currentpage" href="/1/home/">Home</a></li></ol></div>'

Test two-level navigation rendering.

    >>> from django.core import management
    >>> management.call_command('loaddata', 'initial_data.xml', verbosity=0)
    >>> import os.path
    >>> from pages import settings
    >>> from pages.templatetags.navigation import NavigationNode
    >>> from pages.models import Page
    >>> from django.template.context import Context
    >>> nn = NavigationNode(mode="two_level", xml_file=os.path.join(settings.CURDIR, "fixtures", "navigation.xml"))
    >>> c = Context(dict(nav_node=Page.objects.get(id=3)))
    >>> nn.render(c)
    '<div id="two_level"><ul class="main"><li class="sectionlistitem currentsectionlistitem" id="two_level_vestibulum-leo"><a class="section currentsection" href="/2/vestibulum-leo/">Vestibulum Leo</a></li><li class="sectionlistitem" id="two_level_vivamus-gravida-dignissim"><a class="section" href="/20/vivamus-gravida-dignissim/">Vivamus-Gravida Dignissim</a></li><li class="sectionlistitem" id="two_level_maecenas-quis"><a class="section" href="/37/maecenas-quis/">Maecenas Quis</a></li></ul><div id="two_level_vestibulum-leo_menu"><ul><li class="currentpagelistitem" id="two_level_fermentum-viverra"><a class="currentpage" href="/3/fermentum-viverra/">Fermentum Viverra</a></li><li id="two_level_mauris"><a href="/8/mauris/">Mauris</a></li><li id="two_level_quisque-pretium"><a href="/12/quisque-pretium/">Quisque Pretium</a></li><li id="two_level_nulla-quam-sem"><a href="/16/nulla-quam-sem/">Nulla Quam Sem</a></li><li id="two_level_nunc-at-hendrerit-erat"><a href="/17/nunc-at-hendrerit-erat/">Nunc at Hendrerit Erat</a></li><li id="two_level_maecenas-dapibus"><a href="/18/maecenas-dapibus/">Maecenas Dapibus</a></li><li id="two_level_pellentesque-nibh"><a href="/19/pellentesque-nibh/">Pellentesque Nibh</a></li></ul></div><div id="two_level_vivamus-gravida-dignissim_menu"><ul><li id="two_level_curabitur-feugiat"><a href="/21/curabitur-feugiat/">Curabitur Feugiat</a></li><li id="two_level_congue-vel"><a href="/27/congue-vel/">Congue Vel</a></li><li id="two_level_phasellus"><a href="/30/phasellus/">Phasellus</a></li><li id="two_level_porttitor-et-interdum"><a href="/35/porttitor-et-interdum/">Porttitor Et Interdum</a></li></ul></div><div id="two_level_maecenas-quis_menu"><ul><li id="two_level_nulla-commodo-nisl"><a href="/38/nulla-commodo-nisl/">Nulla Commodo Nisl</a></li><li id="two_level_accumsan-vulputate"><a href="/39/accumsan-vulputate/">Accumsan Vulputate</a></li><li id="two_level_lobortis-rhoncus"><a href="/40/lobortis-rhoncus/">Lobortis Rhoncus</a></li><li id="two_level_purus-ut-gravida-iaculis"><a href="/41/purus-ut-gravida-iaculis/">Purus Ut Gravida Iaculis</a></li><li id="two_level_hendrerit"><a href="/42/hendrerit/">Hendrerit</a></li></ul></div></div>'
    >>> c = Context(dict(nav_node=Page.objects.get(id=2)))
    >>> nn.render(c)
    '<div id="two_level"><ul class="main"><li class="sectionlistitem currentsectionlistitem currentpagelistitem" id="two_level_vestibulum-leo"><a class="section currentsection currentpage" href="/2/vestibulum-leo/">Vestibulum Leo</a></li><li class="sectionlistitem" id="two_level_vivamus-gravida-dignissim"><a class="section" href="/20/vivamus-gravida-dignissim/">Vivamus-Gravida Dignissim</a></li><li class="sectionlistitem" id="two_level_maecenas-quis"><a class="section" href="/37/maecenas-quis/">Maecenas Quis</a></li></ul><div id="two_level_vestibulum-leo_menu"><ul><li id="two_level_fermentum-viverra"><a href="/3/fermentum-viverra/">Fermentum Viverra</a></li><li id="two_level_mauris"><a href="/8/mauris/">Mauris</a></li><li id="two_level_quisque-pretium"><a href="/12/quisque-pretium/">Quisque Pretium</a></li><li id="two_level_nulla-quam-sem"><a href="/16/nulla-quam-sem/">Nulla Quam Sem</a></li><li id="two_level_nunc-at-hendrerit-erat"><a href="/17/nunc-at-hendrerit-erat/">Nunc at Hendrerit Erat</a></li><li id="two_level_maecenas-dapibus"><a href="/18/maecenas-dapibus/">Maecenas Dapibus</a></li><li id="two_level_pellentesque-nibh"><a href="/19/pellentesque-nibh/">Pellentesque Nibh</a></li></ul></div><div id="two_level_vivamus-gravida-dignissim_menu"><ul><li id="two_level_curabitur-feugiat"><a href="/21/curabitur-feugiat/">Curabitur Feugiat</a></li><li id="two_level_congue-vel"><a href="/27/congue-vel/">Congue Vel</a></li><li id="two_level_phasellus"><a href="/30/phasellus/">Phasellus</a></li><li id="two_level_porttitor-et-interdum"><a href="/35/porttitor-et-interdum/">Porttitor Et Interdum</a></li></ul></div><div id="two_level_maecenas-quis_menu"><ul><li id="two_level_nulla-commodo-nisl"><a href="/38/nulla-commodo-nisl/">Nulla Commodo Nisl</a></li><li id="two_level_accumsan-vulputate"><a href="/39/accumsan-vulputate/">Accumsan Vulputate</a></li><li id="two_level_lobortis-rhoncus"><a href="/40/lobortis-rhoncus/">Lobortis Rhoncus</a></li><li id="two_level_purus-ut-gravida-iaculis"><a href="/41/purus-ut-gravida-iaculis/">Purus Ut Gravida Iaculis</a></li><li id="two_level_hendrerit"><a href="/42/hendrerit/">Hendrerit</a></li></ul></div></div>'
    >>> c = Context(dict(nav_node=Page.objects.get(id=1)))
    >>> nn.render(c)
    '<div id="two_level"><ul class="main"><li class="sectionlistitem" id="two_level_vestibulum-leo"><a class="section" href="/2/vestibulum-leo/">Vestibulum Leo</a></li><li class="sectionlistitem" id="two_level_vivamus-gravida-dignissim"><a class="section" href="/20/vivamus-gravida-dignissim/">Vivamus-Gravida Dignissim</a></li><li class="sectionlistitem" id="two_level_maecenas-quis"><a class="section" href="/37/maecenas-quis/">Maecenas Quis</a></li></ul><div id="two_level_vestibulum-leo_menu"><ul><li id="two_level_fermentum-viverra"><a href="/3/fermentum-viverra/">Fermentum Viverra</a></li><li id="two_level_mauris"><a href="/8/mauris/">Mauris</a></li><li id="two_level_quisque-pretium"><a href="/12/quisque-pretium/">Quisque Pretium</a></li><li id="two_level_nulla-quam-sem"><a href="/16/nulla-quam-sem/">Nulla Quam Sem</a></li><li id="two_level_nunc-at-hendrerit-erat"><a href="/17/nunc-at-hendrerit-erat/">Nunc at Hendrerit Erat</a></li><li id="two_level_maecenas-dapibus"><a href="/18/maecenas-dapibus/">Maecenas Dapibus</a></li><li id="two_level_pellentesque-nibh"><a href="/19/pellentesque-nibh/">Pellentesque Nibh</a></li></ul></div><div id="two_level_vivamus-gravida-dignissim_menu"><ul><li id="two_level_curabitur-feugiat"><a href="/21/curabitur-feugiat/">Curabitur Feugiat</a></li><li id="two_level_congue-vel"><a href="/27/congue-vel/">Congue Vel</a></li><li id="two_level_phasellus"><a href="/30/phasellus/">Phasellus</a></li><li id="two_level_porttitor-et-interdum"><a href="/35/porttitor-et-interdum/">Porttitor Et Interdum</a></li></ul></div><div id="two_level_maecenas-quis_menu"><ul><li id="two_level_nulla-commodo-nisl"><a href="/38/nulla-commodo-nisl/">Nulla Commodo Nisl</a></li><li id="two_level_accumsan-vulputate"><a href="/39/accumsan-vulputate/">Accumsan Vulputate</a></li><li id="two_level_lobortis-rhoncus"><a href="/40/lobortis-rhoncus/">Lobortis Rhoncus</a></li><li id="two_level_purus-ut-gravida-iaculis"><a href="/41/purus-ut-gravida-iaculis/">Purus Ut Gravida Iaculis</a></li><li id="two_level_hendrerit"><a href="/42/hendrerit/">Hendrerit</a></li></ul></div></div>'
"""}

__test__['SITEMAP_IMPORT_TESTS'] = """

Testing import of sitemap YAML.

    >>> import os.path
    >>> import elementtree.ElementTree as et
    >>> from pages import settings
    >>> from pages.models import Page
    >>> from pages.management.commands.sitemap import Command as SitemapCommand
    >>> sc = SitemapCommand()
    >>> yaml_text = open(os.path.join(settings.CURDIR, "fixtures", "sitemap.yml")).read()
    >>> tree = sc.parse_sitemap(yaml_text)
    >>> et.tostring(tree.getroot())
    '<menus><menu name="navigation" title="Navigation"><node contenttype="15" href="/1/home/" name="home" objectid="1" title="Home"><node contenttype="15" href="/2/vestibulum-leo/" name="vestibulum-leo" objectid="2" title="Vestibulum Leo"><node contenttype="15" href="/3/fermentum-viverra/" name="fermentum-viverra" objectid="3" title="Fermentum Viverra"><node contenttype="15" href="/4/aliquam-interdum/" name="aliquam-interdum" objectid="4" title="Aliquam Interdum" /><node contenttype="15" href="/5/phasellus-at-nisl/" name="phasellus-at-nisl" objectid="5" title="Phasellus at Nisl" /><node contenttype="15" href="/6/duis-faucibus/" name="duis-faucibus" objectid="6" title="Duis Faucibus" /><node contenttype="15" href="/7/ornare-ultrices-turpis/" name="ornare-ultrices-turpis" objectid="7" title="Ornare Ultrices Turpis" /></node><node contenttype="15" href="/8/mauris/" name="mauris" objectid="8" title="Mauris"><node contenttype="15" href="/9/sodales-vel-viverra/" name="sodales-vel-viverra" objectid="9" title="Sodales Vel Viverra" /><node contenttype="15" href="/10/elementum/" name="elementum" objectid="10" title="Elementum" /><node contenttype="15" href="/11/lectus-felis-vel/" name="lectus-felis-vel" objectid="11" title="Lectus Felis Vel" /></node><node contenttype="15" href="/12/quisque-pretium/" name="quisque-pretium" objectid="12" title="Quisque Pretium"><node contenttype="15" href="/13/metus-et-orci/" name="metus-et-orci" objectid="13" title="Metus Et Orci" /><node contenttype="15" href="/14/lacinia-scelerisque/" name="lacinia-scelerisque" objectid="14" title="Lacinia Scelerisque" /><node contenttype="15" href="/15/nunc-nec-justo/" name="nunc-nec-justo" objectid="15" title="Nunc Nec Justo" /></node><node contenttype="15" href="/16/nulla-quam-sem/" name="nulla-quam-sem" objectid="16" title="Nulla Quam Sem" /><node contenttype="15" href="/17/nunc-at-hendrerit-erat/" name="nunc-at-hendrerit-erat" objectid="17" title="Nunc at Hendrerit Erat" /><node contenttype="15" href="/18/maecenas-dapibus/" name="maecenas-dapibus" objectid="18" title="Maecenas Dapibus" /><node contenttype="15" href="/19/pellentesque-nibh/" name="pellentesque-nibh" objectid="19" title="Pellentesque Nibh" /></node><node contenttype="15" href="/20/vivamus-gravida-dignissim/" name="vivamus-gravida-dignissim" objectid="20" title="Vivamus-Gravida Dignissim"><node contenttype="15" href="/21/curabitur-feugiat/" name="curabitur-feugiat" objectid="21" title="Curabitur Feugiat"><node contenttype="15" href="/22/laoreet-sed-pellentesque/" name="laoreet-sed-pellentesque" objectid="22" title="Laoreet Sed Pellentesque" /><node contenttype="15" href="/23/donec-tempus/" name="donec-tempus" objectid="23" title="Donec Tempus" /><node contenttype="15" href="/24/sollicitudin-sapien/" name="sollicitudin-sapien" objectid="24" title="Sollicitudin Sapien" /><node contenttype="15" href="/25/ut-convallis/" name="ut-convallis" objectid="25" title="Ut Convallis" /><node contenttype="15" href="/26/habitasse/" name="habitasse" objectid="26" title="Habitasse" /></node><node contenttype="15" href="/27/congue-vel/" name="congue-vel" objectid="27" title="Congue Vel"><node contenttype="15" href="/28/nunc-pulvinar-luctus/" name="nunc-pulvinar-luctus" objectid="28" title="Nunc Pulvinar Luctus" /><node contenttype="15" href="/29/habitasse-platea/" name="habitasse-platea" objectid="29" title="Habitasse Platea" /></node><node contenttype="15" href="/30/phasellus/" name="phasellus" objectid="30" title="Phasellus"><node contenttype="15" href="/31/nunc-lacinia-eleifend/" name="nunc-lacinia-eleifend" objectid="31" title="Nunc Lacinia Eleifend" /><node contenttype="15" href="/32/consectetur-magna/" name="consectetur-magna" objectid="32" title="Consectetur Magna" /><node contenttype="15" href="/33/amet-leo-commodo-mattis/" name="amet-leo-commodo-mattis" objectid="33" title="Amet Leo Commodo-Mattis" /><node contenttype="15" href="/34/laoreet-est-cursus/" name="laoreet-est-cursus" objectid="34" title="Laoreet Est Cursus" /></node><node contenttype="15" href="/35/porttitor-et-interdum/" name="porttitor-et-interdum" objectid="35" title="Porttitor Et Interdum"><node contenttype="15" href="/36/fusce-a-purus/" name="fusce-a-purus" objectid="36" title="Fusce a Purus" /></node></node><node contenttype="15" href="/37/maecenas-quis/" name="maecenas-quis" objectid="37" title="Maecenas Quis"><node contenttype="15" href="/38/nulla-commodo-nisl/" name="nulla-commodo-nisl" objectid="38" title="Nulla Commodo Nisl" /><node contenttype="15" href="/39/accumsan-vulputate/" name="accumsan-vulputate" objectid="39" title="Accumsan Vulputate" /><node contenttype="15" href="/40/lobortis-rhoncus/" name="lobortis-rhoncus" objectid="40" title="Lobortis Rhoncus" /><node contenttype="15" href="/41/purus-ut-gravida-iaculis/" name="purus-ut-gravida-iaculis" objectid="41" title="Purus Ut Gravida Iaculis" /><node contenttype="15" href="/42/hendrerit/" name="hendrerit" objectid="42" title="Hendrerit" /></node></node></menu><menu name="not_in_navigation" title="Not In Navigation"><node contenttype="15" href="/43/faucibus-sodales-ornare/" name="faucibus-sodales-ornare" objectid="43" title="Faucibus Sodales Ornare"><node contenttype="15" href="/44/sodales/" name="sodales" objectid="44" title="Sodales" /><node contenttype="15" href="/45/curabitur-tempor-lobortis/" name="curabitur-tempor-lobortis" objectid="45" title="Curabitur Tempor Lobortis"><node contenttype="15" href="/46/donec-fermentum/" name="donec-fermentum" objectid="46" title="Donec Fermentum" /></node><node contenttype="15" href="/47/dolor-bibendum/" name="dolor-bibendum" objectid="47" title="Dolor Bibendum" /><node contenttype="15" href="/48/consectetur-tellus/" name="consectetur-tellus" objectid="48" title="Consectetur Tellus" /><node contenttype="15" href="/49/pellentesque/" name="pellentesque" objectid="49" title="Pellentesque" /></node></menu></menus>'
    >>> Page.objects.get(id=1).title
    u'Home'
    >>> Page.objects.get(id=2).title
    u'Vestibulum Leo'
    >>> Page.objects.get(id=3).title
    u'Fermentum Viverra'
    >>> Page.objects.get(id=4).title
    u'Aliquam Interdum'
    >>> Page.objects.get(id=5).title
    u'Phasellus at Nisl'
    >>> Page.objects.get(id=6).title
    u'Duis Faucibus'
    >>> Page.objects.get(id=7).title
    u'Ornare Ultrices Turpis'
"""