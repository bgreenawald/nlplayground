import os

from quart import Blueprint, render_template, Markup

routes = Blueprint("routes", __name__, static_url_path='', static_folder='assets',)


# Generic routes
@routes.route('/')
def index() -> str:
    """
    The home page route.

    Returns:
        str: The home page template.
    """
    return render_template("index.html")


@routes.route('/sidebar')
def sidebar() -> str:
    """
    Returns the sidebar. Used to keep one version of the sidebar globally.

    Returns:
        str: The sidebar template.
    """
    return render_template('sidebar.html')


@routes.route('/header')
def header() -> str:
    """
    Returns the header. Used to keep one version of the header globally.

    Returns:
        str: The header template.k
    """
    return render_template('header.html')


@routes.route('/games/<name>')
def games(name: str) -> str:
    """
    The games route. Return the correct game page based on the route.

    Args:
        name (str): The name of the game to load.

    Returns:
        str: The template for the corresponding game or the index template if the game
            does not exist.
    """
    name_map = {
        "madgab": 'games/madgab.html',
    }

    if name not in name_map:
        return render_template("index.html")
    else:
        return render_template(name_map[name])


@routes.route('/mixmash/<name>')
def mixmash(name: str) -> str:
    """
    The mix and mash route. Returns the correct mix and mash project based on the
    provided name.

    Args:
        name (str): The name of the mix and mash project to load.

    Returns:
        str: The corresponding mix and mash template or the index template if
            the project is not found.
    """
    if name == "biblicaltrump":
        data = {
            "project_name": "biblical_trump",
            "title": "Biblical Trump",
            "description": Markup("""
                <p>What would Trump sounds like if he tweeted
                during Biblical times?
                This is not meant to be political, just having some fun.
                Read more about the project
                <a href="https://bgreenawald.github.io/blog/2018/markov-text-gen.html">
                here.</a></p>
            """),
            "gallery_description": Markup("""
                <p>See a gallery of some of my favorite biblical Trumpisms.
                Capitalization done manually.</p>
            """),
            "gallery": [
                "Though shalt not go use Twitter Trump",
                "I am the Ephraimites best which was great",
                "The midst of seventy years agothis is mad sometimes referred to be long massive tax just named Eutychus being stubborn can call it",  # noqa: E501
                "The original costume was Susan Berry",
                "Who was a son of them thou shalt thou art not the word again despite Obamas terrible",  # noqa: E501
                "Spectacular panoramic views of the ground",
            ],
            "data": Markup("""
                <p>The data for this project was the Gutenburg Bible and an archive of
                <a href="https://github.com/mkearney/trumptweets">Trump's tweets</a></p>
            """)
        }

        return render_template("mixmash/mixmash.html", **data)
    else:
        return render_template("index.html")


@routes.route('/mixmash')
def mixmash_index() -> str:
    """
    Return the mix and mash homepage.

    Returns:
        str: The mix and mash homepage template.
    """
    return render_template("/mixmash/index.html")


@routes.route('/nntextgen/<name>')
def textgen(name: str) -> str:
    """
    The NN text gen route. Returns the correct nn text gen project based on the
    name.

    Args:
        name (str): The name of the project to load.

    Returns:
        str: The corresponding nn text gen template or the index template if the project
            does not exist.
    """
    data = {
        "boy_names": {
            "project_name": "boy_names",
            "title": "Boy Names",
            "description": Markup("""
                <p>Generates new boy names from a dataset of 1000 boy names.
                Enter some starting characters in the box below to get the
                algorithm started, or leave blank for a random start. Tweak
                the options to your liking and click "Generate" when you're ready!</p>
            """),
            "iters": list(range(1, 11)),
            "selected": 5,
            "gallery_description": Markup("""
                <p>Some of my favorite generated names.</p>
            """),
            "gallery": [
                "AngeldeJesus",
                "Babatunde",
                "Curvin",
                "Deforest",
                "Gobel",
                "Moishy",
                "Purvis",
                "Riggins",
                "Ugo",
                "Yer",
            ],
            "gallery_full": Markup("""
                <a href="/nntextgen/gallery/boy_names">See the full gallery.</a>
            """),
            "data_description": Markup("""
                <p>This model was trained on 1000 boy names from
                <a href="https://www.babble.com/pregnancy/1000-most-popular-boy-names/">
                here.</a></p>
            """),
            "data_full": Markup("""
                <a href="/nntextgen/data/boy_names">See the full data.</a>
            """)
        },
        "girl_names": {
            "project_name": "girl_names",
            "title": "Girl Names",
            "description": Markup("""
                <p>Generates new girls names from a dataset of 1000 girl names.
                Enter some starting characters in the box below to get the
                algorithm started, or leave blank for a random start. Tweak
                the options to your liking and click "Generate" when you're ready!</p>
            """),
            "iters": list(range(1, 11)),
            "selected": 5,
            "gallery_description": Markup("""
                <p>Some of my favorite generated names.</p>
            """),
            "gallery": [
                "Blonnie",
                "Borghild",
                "Jamiracle",
                "Pasqualina",
                "Pearly",
                "Rut",
                "Sharde",
                "Shaquasia",
                "Unnamed",
                "Vanellope",
            ],
            "gallery_full": Markup("""
                <a href="/nntextgen/gallery/girl_names">See the full gallery.</a>
            """),
            "data_description": Markup("""
                <p>This model was trained on 1000 girl names from
                <a href="https://www.babble.com/pregnancy/1000-most-popular-girl-names/">
                here.</a></p>
            """),
            "data_full": Markup("""
                <a href="/nntextgen/data/girl_names">See the full data.</a>
            """)
        },
        "stripper_names": {
            "project_name": "stripper_names",
            "title": "Stripper Names",
            "description": Markup("""
                <p>Generates new stripper names from a dataset of over
                8000 adult film actresses.
                Enter some starting characters in the box below to get the
                algorithm started, or leave blank for a random start. Tweak
                the options to your liking and click "Generate" when you're ready!</p>
            """),
            "iters": list(range(1, 6)),
            "selected": 3,
            "gallery_description": Markup("""
                <p>Some of my favorite generated names.</p>
            """),
            "gallery": [
                "Casolyn Fart",
                "Soxy Black",
            ],
            "gallery_full": Markup("""
                <a href="/nntextgen/gallery/stripper_names">See the full gallery.</a>
            """),
            "data_description": Markup("""
                <p>This model was trained over 8000 adult film actress names scraped
                from various sources.</p>
            """),
            "data_full": Markup("""
                <a href="/nntextgen/data/stripper_names">See the full data.</a>
            """)
        },
        "pokemon_names": {
            "project_name": "pokemon_names",
            "title": "Pokemon Names",
            "description": Markup("""
                <p>Over 800 Pokemon not enough? Generate some new ones!
                Enter some starting characters in the box below to get the
                algorithm started, or leave blank for a random start. Tweak
                the options to your liking and click "Generate" when you're ready!</p>
            """),
            "iters": list(range(1, 11)),
            "selected": 5,
            "gallery_description": Markup("""
                <p>Some of my favorite generated names.</p>
            """),
            "gallery": [
                "Eoaoeo",
                "Gooohu",
                "Vesaggy",
            ],
            "gallery_full": Markup("""
                <a href="/nntextgen/gallery/pokemon_names">See the full gallery.</a>
            """),
            "data_description": Markup("""
                <p>This model was train on all Pokemon names (pre Sword and Shield) from
                <a href="https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name">
                here.</a></p>
            """),
            "data_full": Markup("""
                <a href="/nntextgen/data/pokemon_names">See the full data.</a>
            """)
        },
        "dinosaur_names": {
            "project_name": "dinosaur_names",
            "title": "Dinosaur Names",
            "description": Markup("""
                <p>Need some inspiration for you latest prehistoric archaeological
                discover? Generate yourself some new dinosaurs names!
                Enter some starting characters in the box below to get the
                algorithm started, or leave blank for a random start. Tweak
                the options to your liking and click "Generate" when you're ready!</p>
            """),
            "iters": list(range(1, 6)),
            "selected": 3,
            "gallery_description": Markup("""
                <p>Some of my favorite generated names.</p>
            """),
            "gallery": [
                "Dampylodon",
                "Lemopus",
                "Shamag",
            ],
            "gallery_full": Markup("""
                <a href="/nntextgen/gallery/dinosaur_names">See the full gallery.</a>
            """),
            "data_description": Markup("""
                <p>This model was trained on over 1500 dinosaur names from
                <a href="https://en.wikipedia.org/wiki/List_of_dinosaur_genera">here.
                </a></p>
            """),
            "data_full": Markup("""
                <a href="/nntextgen/data/dinosaur_names">See the full data.</a>
            """)
        },

    }
    if name in data:
        return render_template("/nntextgen/nntextgen.html", **data[name])
    else:
        return render_template("index.html")


@routes.route('/nntextgen')
def nntextgen_index() -> str:
    """
    The home page for the nn text gen project.

    Returns:
        str: The home page template for nn text gen.
    """
    return render_template("/nntextgen/index.html")


@routes.route('/nntextgen/data/<name>')
def data(name: str) -> str:
    """
    Data endpoint for nn text gen projects.

    Args:
        name (str): The name of the nn text project to get data for.

    Returns:
        str: The populated data template for the given nn text gen project, or
            an error template if the given project is not found.
    """
    project_info = {
        "boy_names": ("Boy Names", Markup("""
            <p>This model was trained on 1000 boy names from
            <a href="https://www.babble.com/pregnancy/1000-most-popular-boy-names/">here.</a></p>
        """)),
        "girl_names": ("Girl Names", Markup("""
            <p>This model was trained on 1000 girl names from
            <a href="https://www.babble.com/pregnancy/1000-most-popular-girl-names/">here.</a></p>
        """)),
        "stripper_names": ("Stripper Names", Markup("""
            <p>This model was trained on 8000 adult film actress names from a
            variety of sources.</p>
        """)),
        "pokemon_names": ("Pokemon Names", Markup("""
            <p>This model was train on all Pokemon names (pre Sword and Shield) from
            <a href="https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name">
            here.</a></p>
        """)),
        "dinosaur_names": ("Dinosaur Names", Markup("""
            <p>This model was trained on over 1500 dinosaur names from
            <a href="https://en.wikipedia.org/wiki/List_of_dinosaur_genera">here.</a></p>
        """)),
    }

    filename = f"data/nntextgen/{name}/data.txt"

    if os.path.exists(filename) and name in project_info:
        with open(filename, "r") as file:
            data = file.read().split("\n")
        ret = {
            "title": project_info[name][0],
            "data_description": project_info[name][1],
            "data": data
        }
    else:
        ret = {
            "title": "Error",
            "data_description": "A dataset for the given project does not exist",
            "data": []
        }

    return render_template("/nntextgen/data.html", **ret)


@routes.route('/nntextgen/gallery/<name>')
def gallery(name: str) -> str:
    """The gallery endpoint for the nn text gen project.

    Args:
        name (str): The name of the project to load the gallery for.

    Returns:
        str: The populated gallery template for the given project, or an error template
            if the project is not found.
    """
    project_info = {
        "boy_names": ("Boy Names", "9000 boy names generated from the model."),
        "girl_names": ("Girl Names", "9000 girl names generated from the model."),
        "stripper_names": ("Stripper Names", "Over 1000 stripper names generated from the model."),
        "pokemon_names": ("Pokemon Names", "Over 500 Pokemon names generated from the model."),
    }

    filename = f"data/nntextgen/{name}/gallery.txt"

    if os.path.exists(filename) and name in project_info:
        with open(filename, "r") as file:
            data = file.read().split("\n")
        ret = {
            "title": project_info[name][0],
            "gallery_description": project_info[name][1],
            "gallery": data
        }
    else:
        ret = {
            "title": "Error",
            "data_description": "A gallery for the given project does not exist",
            "data": []
        }

    return render_template("/nntextgen/gallery.html", **ret)
