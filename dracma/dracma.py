import os
import sys
import dracma_CLI


def first_initialization() -> None:
    file = open("config.json", "w")
    
    match sys.argv[1].strip().lower():
        case "cli":
            dracma_CLI.first_initialization()
        
        case _: print("Broo, whaaat??")

    file.close()
    return


def initialize() -> None:
    # Check if the database exist:    
    if not os.path.exists("./config.json"):
        # If this happens, than it's the first initialization
        first_initialization()
    
    if not os.path.exists("./database/acquisitions.db"):
        # Create databases...
        # This should only happen in the first initialization or if the user broke something...
        ...

    return


def terminate() -> None:
    # Check if all opened files are closed:
    ...

    # Print a random goodbye message:
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
    initialize()
    main()
