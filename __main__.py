import time
import sys

from info import Info

def main():
    try:
        info = Info()
        time.sleep(1)
        info.retrieve_info()
    except EOFError:
        print("\nRun this Docker image with -it!")
        sys.exit(-2)
    except KeyboardInterrupt:
        print("\nControl + C has been invoked!")
        sys.exit(-3)
    except Exception:
        print("\nSomething went wrong!")
        sys.exit(-1)

if __name__ == "__main__":
    main()
