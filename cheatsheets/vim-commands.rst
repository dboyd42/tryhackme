Vim-Commands
############
:Author: David Boyd
:Date: 2020-06-01

set linebreak (lbr)
-------------------

	Will wrap long lines at a character in 'breat' rather than at the last character that fits on the screen.

:put=strftime('%F')
-------------------

	- Vim's built-in date formatter.
	- Puts string fns time Full date into document.
	- I.e) 2020-06-01


:.s/./#/g -OR- :.s/./=/g -OR- :.s/./-/g
---------------------------------------

	- .rst files
	- substitutes line for a RST header
	- use in conjuction with yy
	- nnoremap y- yyp:.s/./-/g<CR> && nohls<CR>
	- nnoremap y= yyp:.s/./=/g<CR> && nohls<CR>
	- nnoremap y+ yyp:.s/./+/g<CR> && nohls<CR>

:.s/^-\+$/<substitution>/g
--------------------------

	- replace entire line of repeated char "=" with <substitution>

set <setting>?
--------------

	- Get current value of setting

set formatoptions(+/-)=t
------------------------
:see: https://vim.fandom.com/wiki/Automatic_word_wrapping

	- == set fo
	- set formatoptions?		// get current settings
	- set formatoptions+=t		// add letter to   formatoptions
	- set formatoptions-=l		// rm  letter from formatoptions

gggqG
-----

	- reformat entire document  // must prev set formatoptions,tw,etc.
	- gg: goto beginning of buffer
	- gq: reformat the text included in the motion
	- G : goto end of buffer



inoremap <S-CR> <CR><CR><CR><BS>
--------------------------------

	- insert two spaces between lines && del tab space
	- used to divide prev answers > next questions


