from bs4 import BeautifulSoup
import requests



class AssetCollector:

	FILE_COUNT = 0

	def __init__(self, url):
		self.url = url

	def fetch_assets(self):
		url = self.url

		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")

		img_tags = soup.find_all('img')

		for img_tag in img_tags:
			img_src = img_tag.get("src")

			if self.is_url(img_src):
				self.write_image(self.get_url_content(img_src), f'asset-{self.FILE_COUNT}.png')
			elif self.is_svg(img_src):
				svg_extract = self.format_svg(img_src)
				self.write_image(svg_extract, f'asset-{self.FILE_COUNT}.svg', mode="w")

			self.FILE_COUNT += 1

	def get_url_content(self, url:str):
		response = requests.get(url)

		return response.content

	def is_url(self, text:str):
		if text.startswith('http'):
			return True
		return False

	def is_svg(self, text:str):
		if text.startswith('data:image/svg+xml'):
			return True
		return False

	def format_svg(self, text:str):
		return requests.utils.unquote(text).strip().split(',')[-1]

	def write_image(self, content:str, filename:str, mode="wb"):
		with open(filename, mode) as file:
			file.write(content)



def main():
	url = input("Enter website url : ")
	collector = AssetCollector(url)
	collector.fetch_assets()


if __name__ == "__main__":
	main()
