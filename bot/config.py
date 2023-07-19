import os


class Config:

    BOT_TOKEN = "6384620993:AAG1-lGVb0H-QgWUbZPDeJwt6BT_vGH9NF8"

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = "11304655"

    API_HASH = "88ff4601886955f1111c9f5b14bf0245"

    CLIENT_ID = "1041194362169-ljnr28h7226k09kkq4erpp8euvo7brhk.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "1547312047"

    AUTH_USERS_TEXT = "1547312047"

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
