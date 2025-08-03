import wikipedia

def main():
    while True:
        search_phrase = input("Enter a Wikipedia page title or search phrase (blank to quit): ").strip()
        if not search_phrase:
            print("Goodbye!")
            break
        try:
            # 关闭自动suggest，严格按照输入查询
            page = wikipedia.page(search_phrase, autosuggest=False)
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation page found. Options: {e.options[:5]} ...")
            continue
        except wikipedia.PageError:
            print("Page not found. Please try again.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        print(f"\n--- Page details ---")
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary[:200]}{'...' if len(page.summary)>200 else ''}")
        print(f"URL: {page.url}\n")

if __name__ == "__main__":
    main()