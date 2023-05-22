// lazyload config
var MODULE_CONFIG = {
    fullscreen:     [
                      '../static/libs/jquery-fullscreen-plugin/jquery.fullscreen-min.js',
                      '../static/assets/js/plugins/fullscreen.js'
                    ],
    jscroll:        [
                      '../static/libs/jscroll/dist/jquery.jscroll.min.js'
                    ],
    dataTable:      [
                      '../static/libs/datatables/media-table/js/jquery.dataTables.min.js',
                      '../static/libs/datatables.net-bs4/js/dataTables.bootstrap4.min.js',
                      '../static/libs/datatables.net-bs4/css/dataTables.bootstrap4.min.css',
                      '../static/assets/js/plugins/datatable.js'
                    ],
    stellar:        [
                      '../static/libs/jquery.stellar/jquery.stellar.min.js',
                      '../static/assets/js/plugins/stellar.js'
                    ],
    typeahead:      [
                      '../static/libs/typeahead.js/dist/typeahead.bundle.min.js',
                      '../static/assets/js/plugins/typeahead.js'
                    ],
    user:           [
                      '../static/libs/list.js/dist/list.js',
                      '../static/assets/js/app/user.js'
                    ],
  };

var MODULE_OPTION_CONFIG = {
  parsley: {
    errorClass: 'is-invalid',
    successClass: 'is-valid',
    errorsWrapper: '<ul class="list-unstyled text-sm mt-1 text-muted"></ul>'
  }
}
