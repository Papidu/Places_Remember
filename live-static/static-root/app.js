new Vue({
    el: '#form',
    data: {
        orders: []
    },
    created: function(){
        const vm = this;
        axios.get('/api/aremembercards')
        .then(function(response){
         vm.orders = response.data
        })
    }
}
)