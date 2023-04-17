import flask


app = flask.Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/channel/<name>/")
def channel_name(name):
    messages = flask._app_ctx_stack.channels[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys()) if flask._app_ctx_stack.groups else {}
    dm_users = list(flask._app_ctx_stack.dm_users) if hasattr(flask._app_ctx_stack, "dm_users") else {}
    mpim_users = list(flask._app_ctx_stack.mpim_users) if hasattr(flask._app_ctx_stack, "mpim_users") else {}

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups) if groups else {},
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/group/<name>/")
def group_name(name):
    messages = flask._app_ctx_stack.groups[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users) if hasattr(flask._app_ctx_stack, "dm_users") else {}
    mpim_users = list(flask._app_ctx_stack.mpim_users) if hasattr(flask._app_ctx_stack, "mpim_users") else {}

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/dm/<id>/")
def dm_id(id):
    messages = flask._app_ctx_stack.dms[id]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users) if hasattr(flask._app_ctx_stack, "dm_users") else {}
    mpim_users = list(flask._app_ctx_stack.mpim_users) if hasattr(flask._app_ctx_stack, "mpim_users") else {}

    return flask.render_template("viewer.html", messages=messages,
                                 id=id.format(id=id),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/mpim/<name>/")
def mpim_name(name):
    messages = flask._app_ctx_stack.mpims.get(name, list())
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users) if hasattr(flask._app_ctx_stack, "dm_users") else {}
    mpim_users = list(flask._app_ctx_stack.mpim_users) if hasattr(flask._app_ctx_stack, "mpim_users") else {}

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/")
def index():
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    
    if hasattr(flask._app_ctx_stack, "dms"):
        dms = list(flask._app_ctx_stack.dms.keys())
    if hasattr(flask._app_ctx_stack, "mpims"):
        mpims = list(flask._app_ctx_stack.mpims.keys())
    if channels:
        if "general" in channels:
            return channel_name("general")
        else:
            return channel_name(channels[0])
    elif groups:
        return group_name(groups[0])
    elif hasattr(flask._app_ctx_stack, "dms") and dms:
        return dm_id(dms[0])
    elif hasattr(flask._app_ctx_stack, "mpims") and mpims:
        return mpim_name(mpims[0])
    else:
        return "No content was found in your export that we could render."
