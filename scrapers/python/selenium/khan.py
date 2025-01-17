import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chromedriver_autoinstaller.install()
# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path


def get_energy_points(user):
    """Return the wonderful energy points."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(f"https://www.khanacademy.org/profile/{user}/")
    try:
        energy_points_elem = driver.find_element_by_css_selector(".energy-points-badge")
        return energy_points_elem.text
    except NoSuchElementException as nosee:
        print(str(nosee))
        return "Could not find Energy Points Element. "


def main():
    user = "johnbampton"
    profile_energy = get_energy_points(user)
    print(f"User => {user} ; Energy Point => {profile_energy} ;")


if __name__ == "__main__":
    main()
