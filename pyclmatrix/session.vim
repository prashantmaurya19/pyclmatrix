let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +26 __init__.py
badd +30 _globals.py
badd +60 _kernel.py
badd +7 ~/Downloads/codebase/MyPy/modules/pyclmatrix/test/setup.py
badd +1 ~/Downloads/codebase/MyPy/modules/pyclmatrix/Makefile
badd +1 ~/Downloads/codebase/MyPy/modules/pyclmatrix/test/__main__.py
badd +2 ~/Downloads/codebase/MyPy/modules/pyclmatrix/testing/__main__.py
badd +1 ~/Downloads/codebase/MyPy/modules/pyclmatrix/testing/setup.py
badd +1 testing/__main__.py
badd +2 testing/setup.py
badd +0 
badd +3 testing/kernels_test.py
badd +36 utils.py
argglobal
%argdel
$argadd 
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit __init__.py
argglobal
balt _globals.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 8 - ((7 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 0
lcd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
tabnext
edit ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/utils.py
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 36 - ((22 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 36
normal! 05|
lcd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
tabnext
edit ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/_globals.py
argglobal
balt ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/__init__.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 30 - ((11 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 30
normal! 0
lcd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
tabnext
edit ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/_kernel.py
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 60 - ((23 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 60
normal! 0
lcd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
tabnext
edit ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/testing/kernels_test.py
argglobal
balt ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix/_kernel.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 3 - ((2 * winheight(0) + 12) / 24)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 3
normal! 050|
lcd ~/Downloads/codebase/MyPy/modules/pyclmatrix/pyclmatrix
tabnext 5
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
