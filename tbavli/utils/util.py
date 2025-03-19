import socket

class Util:
    """Holds utility functions."""

    @staticmethod
    def get_host(name: str) -> bytes:
        """
        Get the host of a given name.

        Args:
            name (str): The name to get the host of.

        Returns:
            bytes: The host of the given name.

        Raises:
            RuntimeError: If the host cannot be found.
        """
        try:
            return socket.gethostbyname(name).encode()  # Convert IP to bytes
        except socket.gaierror as e:
            raise RuntimeError(e)