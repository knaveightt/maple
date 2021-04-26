;;; knv-workspaces.el -- collection of startup functions per project

;;; Commentary:
;;; Defines functions that, when called as part of executing Emacs (e.g. Emacs -f <function>),
;;; will run some pre-defined sequence of actions to setup the workspace specific for a given project.

;;; Code:
(defun project-open-totalknavery()
  "Opens totalknavery project default file and neotree."
  (find-file "~/Projects/totalknavery2/totalknavery/index.html")
  (neotree-show)
  )

(provide 'knv-workspaces)
;;; knv-workspaces.el ends here
