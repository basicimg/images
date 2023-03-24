import yaml

def get_latest_jdk(distroJdks):
    latest = None
    latestInt = 0
    for jdk in distroJdks:
        if jdk == "latest":
            latest = jdk
            latestInt = 999
        elif int(jdk) > latestInt:
            latest = jdk
            latestInt = int(jdk)
    return latest

def get_lts_jdk(jdks, distroJdks):
    latest = None
    latestInt = 0
    for jdk in distroJdks:
        if jdk != "latest" and int(jdk) > latestInt and jdks[jdk]["lts"]:
            latest = jdk
            latestInt = int(jdk)
    return latest

def generate_jdk_images(path):
    with open(path, "r") as stream:
        defs = yaml.safe_load(stream)
    jdks = defs["jdks"]
    distros = defs["distros"]
    images = []
    for distro in distros:
        name = distro["name"]
        base = distro["base"]
        default = False
        if "default" in distro:
            default = distro["default"]
        aliases = [name]
        if "aliases" in distro:
            aliases.extend(distro["aliases"])
        distroJdks = distro["jdks"]
        latest = get_latest_jdk(distroJdks)
        lts = get_lts_jdk(jdks, distroJdks)
        for jdk in distroJdks:
            isLatest = jdk == latest
            isLts = jdk == lts
            tags = []
            for alias in aliases:
                tags.append(f"{jdk}-{alias}")
                if isLatest and jdk != "latest":
                    tags.append(f"latest-{alias}")
                if isLts:
                    tags.append(f"lts-{alias}")
                    tags.append(alias)
            if default:
                tags.append(jdk)
                if isLatest:
                    tags.append("latest")
                if isLts:
                    tags.append("lts")
            fullTags = [f"ghcr.io/basicimg/jdk:{tag}" for tag in tags]
            images.append({
                "path": f"jdk/{jdk}/{name}",
                "generate": True,
                "base": base,
                "install": [distroJdks[jdk]],
                "app": "$(java -version 2>&1 | head -n 1)",
                "tags": fullTags,
                "description": f"JDK {jdk} installed on {name}"
            })
    return images
