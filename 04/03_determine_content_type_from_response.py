from util import const
from util.urls import URLUtility

util = URLUtility(const.ApodEclipseImage())
print(f"The content type is: {util.contenttype}")

