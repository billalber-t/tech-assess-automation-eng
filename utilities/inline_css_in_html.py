import os

def inline_css_in_html(html_file_path, css_folder_path):
    # Read the HTML file
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()

    # Read and inline all CSS files in the assets folder
    css_files = [f for f in os.listdir(css_folder_path) if f.endswith('.css')]
    css_styles = ""
    for css_file in css_files:
        css_file_path = os.path.join(css_folder_path, css_file)
        with open(css_file_path, 'r') as file:
            css_styles += file.read()

    # Insert CSS into HTML
    css_style_tag = f'<style>{css_styles}</style>'
    updated_html_content = html_content.replace('</head>', f'{css_style_tag}</head>')

    # Save the updated HTML file
    with open(html_file_path, 'w') as html_file:
        html_file.write(updated_html_content)

# Usage




if __name__ == "__main__":
    # Set the email details
    html_report_path = 'report/report.html'
    css_folder_path = 'report/assess'
    inline_css_in_html(html_report_path, css_folder_path)

