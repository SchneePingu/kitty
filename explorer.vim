function! KittyExplorePath()
  let grepResult = getline('.')
  let bashCommandToGetLineNumberAndPath = "echo ".grepResult." | sed -E 's/(^.*)[:|-]([0-9]+)[:|-].*$/+:\\2 \\1/'"
  let vimCommandToOpenPath = ":tabe ".system(bashCommandToGetLineNumberAndPath)
  execute vimCommandToOpenPath
endfunction

