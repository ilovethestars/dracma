import sys
import dracma_CLI


def terminate() -> None:
    print("You'll be back...") # TODO make cool random messages
    sys.exit(0)

    return


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Input required. Use \"python dracma.py <input>\" instead.\n"
            "For a list of available commands, check the software's manual."
        ) # TODO make software manual :p
        sys.exit(1)

    match sys.argv[1].strip().lower():
        case "cli":
            dracma_CLI.start_application()

        case _:
            ...

    return


if __name__ == "__main__":
    main()