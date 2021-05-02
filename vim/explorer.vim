function! KittyGoToSelectedFile()
  let grepResult = getline('.')
  let bashCommandToGetLineNumberAndPath = "echo '".grepResult."' | sed -E 's/(^.*)[:|-]([0-9]+)[:|-].*$/+:\\2 \\1/'"
  let vimCommandToOpenPath = ":tabe ".system(bashCommandToGetLineNumberAndPath)
  execute vimCommandToOpenPath
endfunction

function! KittyGoToNextSearchResult()
  if search(g:kittySearchPattern, '', line("."))
  else
    call search('^\./.*\:[0-9]\+\:', 'e')
    call search(g:kittySearchPattern, '')
  endif
endfunction

nnoremap <c-h> :q!<CR>
nnoremap <c-l> :call KittyGoToSelectedFile()<CR>
nnoremap <silent> <c-j> :silent! call KittyGoToNextSearchResult()<CR>
