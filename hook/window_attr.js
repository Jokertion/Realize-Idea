var window_flag_1 = 't';
var window_flag_2 = 'ccc';

var key_value_map = {};
var window_value = window[window_flag_1];

Object.defineProperty(window, window_flag_1, {
    get: function() {
        console.log('Getting', window, window_flag_1, '=', window_value);
         debugger;
        return window_value;
    },
    set: function(val) {
        console.log('Setting', window, window_flag_1, '=', val);
         debugger;
        window_value = val;
        key_value_map[window[window_flag_1]] = window_flag_1;
        set_obj_attr(window[window_flag_1], window_flag_2);
    },
});

function set_obj_attr(obj, attr){
    var obj_attr_value = obj[attr];
    Object.defineProperty(obj, attr, {
        get: function() {
            console.log('Getting', key_value_map[obj], attr, '=', obj_attr_value);
//             debugger;
            return obj_attr_value;
        },
        set: function(val) {
            console.log('Setting', key_value_map[obj], attr, '=', val);
//             debugger;
            obj_attr_value = val;
        },
    });
}
