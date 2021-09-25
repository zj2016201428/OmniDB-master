# -*- mode: python -*-

block_cipher = None

data_files = [
  ('omnidb.db','.'),
  ('config.py','.'),
  ('OmniDB_app/static','OmniDB_app/static'),
  ('OmniDB_app/include','OmniDB_app/include'),
  ('OmniDB_app/templates','OmniDB_app/templates'),
  ('OmniDB_app/plugins','OmniDB_app/plugins'),
]

a = Analysis(['omnidb-server.py'],
             pathex=['OmniDB_app/include/'],
             binaries=[],
             datas=data_files,
             hiddenimports=['cheroot.ssl','cheroot.ssl.builtin','psycopg2','paramiko'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)

exe = EXE(pyz,
         a.scripts,
         [],
         a.binaries,
         a.zipfiles,
         a.datas,
         name='omnidb-server',
         debug=False,
         strip=False,
         upx=True,
         runtime_tmpdir=None,
         console=True )
