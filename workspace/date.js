Date.prototype.getJulian = function() {
    return Math.floor((this / 86400000) -
    (this.getTimezoneOffset()/1440) + 2440587.5);
}