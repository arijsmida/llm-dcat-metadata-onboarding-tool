CSS = """
<style>
header, footer { visibility: hidden; }
[data-testid="stSidebar"] { display: none !important; }
.stApp { background-color: white; }

.fixed-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 240px;
    height: 100vh;
    background: #84bd00;
    z-index: 1000;
}

.sidebar-logo {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 35px;
}

.sidebar-logo img {
    width: 215px;
    height: auto;
    object-fit: contain;
}

.topbar {
    margin-left: 240px;
    padding-top: 55px;
    padding-left: 28px;
    padding-bottom: 25px;
    background: white;
}

.topbar-title {
    font-size: 38px;
    font-weight: 900;
    color: #061124;
}

.topbar-subtitle {
    font-size: 14px;
    color: #64748b;
    margin-top: 14px;
}

.block-container {
    padding-top: 20px !important;
    padding-left: 305px !important;
    padding-right: 40px !important;
    max-width: none !important;
}

.section-title {
    color: #84bd00;
    font-size: 22px;
    font-weight: 900;
    margin-top: 10px;
    margin-bottom: 26px;
}

.stButton > button {
    border-radius: 8px !important;
    padding: 12px 24px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    border: 1px solid #d9dee7 !important;
}

.st-key-generate_btn button {
    background-color: #84bd00 !important;
    color: white !important;
    border: none !important;
    height: 50px !important;
}

.st-key-clear_btn button {
    background-color: white !important;
    color: #1f2937 !important;
    border: 1px solid #d9dee7 !important;
    height: 50px !important;
}

div[data-testid="stDownloadButton"] button {
    background-color: #84bd00 !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: bold !important;
}

pre, code {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
}
</style>
"""