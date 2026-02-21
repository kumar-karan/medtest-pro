from playwright.sync_api import sync_playwright
import os

def run():
    os.makedirs("verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # 1. Landing Page
        page.screenshot(path="verification/1_landing_page.png")
        print("Screenshot 1 taken: Landing Page")

        # 2. Modal
        page.click("text=How to Generate Quiz JSON?")
        page.wait_for_selector("#instructions-modal")
        page.screenshot(path="verification/2_modal.png")
        print("Screenshot 2 taken: Modal")

        page.click("#instructions-modal button") # Close modal

        # 3. Upload JSON and Setup Page
        page.set_input_files("#file-json", "dev/example_quiz.json")
        page.wait_for_selector("#btn-start-app:not([disabled])", timeout=5000)
        page.screenshot(path="verification/3_setup_ready.png")
        print("Screenshot 3 taken: Setup Ready")

        # 4. Quiz Interface
        page.click("#btn-start-app")
        page.wait_for_selector("#quiz-content")
        page.screenshot(path="verification/4_quiz_interface.png")
        print("Screenshot 4 taken: Quiz Interface")

        browser.close()

if __name__ == "__main__":
    run()
