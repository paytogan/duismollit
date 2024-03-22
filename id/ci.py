def start_driver(name, id_):
    """
    Start a driver with a given name and id.

    Args:
        name (str): The name of the driver.
        id_ (int): The id of the driver.

    Returns:
        Driver: The driver object.
    """

    driver = Driver(name, id_)
    driver.start()
    return driver

