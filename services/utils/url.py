def build_url_args_from_dict(params: dict) -> str:
    return "&".join([f"{key}={value}" for key, value in params.items()])
