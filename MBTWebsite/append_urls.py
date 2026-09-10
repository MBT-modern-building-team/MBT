with open('MBTApp/urls.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_urls = """    path('admin-budowa/tablice/<str:board_type>/podglad/', oznakowanieViews._board_preview_view, name='board_preview'),
    path('admin-budowa/tablice/<str:board_type>/pobierz/', oznakowanieViews._board_download_view, name='board_download'),
]"""
content = content.replace("]", new_urls, 1)

with open('MBTApp/urls.py', 'w', encoding='utf-8') as f:
    f.write(content)
