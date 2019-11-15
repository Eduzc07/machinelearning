from app import app # Import app to use routes

# ======== Main ============================================================== #
if __name__ == "__main__":
    # app.run(use_reloader=True)
    # app.run(debug=True, use_reloader=True)
    app.run(host= '0.0.0.0', use_reloader=True)
    #app.run(host="127.0.0.1", port=5000, debug=True)
    #app.run(host="127.0.0.1", port=5000, debug=False)
