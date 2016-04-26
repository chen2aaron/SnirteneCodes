Vue.config.delimiters = ['${', '}'];

var paginationVM = new Vue({
    el: '#pagination',
    data: {
        url: '',
        params: {},
        items: [],
        num_page: ''
    },
    computed: {
        page_range: function () {
            var left = 1,
                right = this.num_page,
                ar = [];
            if (this.num_page >= 11) {
                if (this.params.page > 5 && this.params.page < this.num_page - 4) {
                    left = this.params.page - 5;
                    right = this.params.page + 4;
                } else {
                    if (this.params.page <= 5) {
                        left = 1;
                        right = 10;
                    } else {
                        right = this.num_page;
                        left = this.num_page - 9;
                    }
                }
            }
            while (left <= right) {
                ar.push(left);
                left++
            }
            return ar
        },
        showLast: function () {
            return this.params.page != this.num_page;
        },
        showFirst: function () {
            return this.params.page != 1;
        }
    },
    methods: {
        pageClick: function (cur_page) {
            if (cur_page != this.params.page) {
                this.params.page = cur_page;
                var params = this.params;
                params.page = this.params.page;
                this.params = params;
            }
        },
        refresh: function () {
            var self = this;
            $.get(self.url).done(function (page) {
                self.params.page = page.result.page;
                self.items = page.result.data;
                self.num_page = page.result.num_page;
            })
        }
    },
    watch: {
        params: {
            handler: function (newValue) {
                var self = this;
                $.get(self.url + '?' + $.param(newValue)).done(function (page) {
                    self.items = page.result.data;
                    self.num_page = page.result.num_page;
                })
            },
            deep: true
        }
    }
});
