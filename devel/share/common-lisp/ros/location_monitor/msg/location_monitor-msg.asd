
(cl:in-package :asdf)

(defsystem "location_monitor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "landmarkDistance" :depends-on ("_package_landmarkDistance"))
    (:file "_package_landmarkDistance" :depends-on ("_package"))
  ))