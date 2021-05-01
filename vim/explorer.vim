function! KittyGoToSelectedFile()
  let grepResult = getline('.')
  let bashCommandToGetLineNumberAndPath = "echo '".grepResult."' | sed -E 's/(^.*)[:|-]([0-9]+)[:|-].*$/+:\\2 \\1/'"
  let vimCommandToOpenPath = ":tabe ".system(bashCommandToGetLineNumberAndPath)
  execute vimCommandToOpenPath
endfunction

function! KittyGoToNextSearchResult()
  call search('./\/.*\:[0-9]\+\:')
  normal 2t:
  call search(g:kittysearchpattern)
endfunction

nnoremap <c-y> :q!<CR>
nnoremap <c-x> :call KittyGoToSelectedFile()<CR>
nnoremap <silent> <c-@> :silent! call KittyGoToNextSearchResult()<CR>
