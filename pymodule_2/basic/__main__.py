from basic import init_api


def main():
    app = init_api()
    app.run(port=8082, debug=False)


if __name__ == "__main__":
    main()
