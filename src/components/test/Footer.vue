<template>
    <header>
        <p>{{copyright}} {{title}}</p>
    </header>
</template>

<script>
import { bus} from '../../main';
export default {
    props:{
        title:{
            type: String
        }
    },
    data(){
        return {
            copyright: 'Copyright 2019'
        }
    },
    created(){
        bus.$on('titleChanged',(data) => {
            this.title = data
        });
    }
}
</script>

<style scoped>
footer{
    background: #222;
    padding: 6px;
}

p{
    color: #222;
    text-align:center;
}
</style>