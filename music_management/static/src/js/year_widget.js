odoo.define('music_management.year_format', function (require) {
    "use strict";

    var fieldRegistry = require('web.field_registry');
    var DateWidget = require('web.datepicker').DateWidget;
    var FieldDate = require('web.basic_fields').FieldDate;
    var time = require('web.time');

    // Modified DateWidget to be used for year only
    var YearDateWidget = DateWidget.extend({

        _parseYearDate: function (value, field, options) {
            if (!value) {
                return false;
            }
            var datePattern = this.options.format;
            var date;
            if (options && options.isUTC) {
                date = moment.utc(value);
            } else {
                date = moment.utc(value, [datePattern, moment.ISO_8601], true);
            }
            if (date.isValid()) {
                if (date.year() >= 1900) {
                    date.toJSON = function () {
                        return this.clone().locale('en').format('YYYY');
                    };
                    return date;
                }
            }
            throw new Error(_.str.sprintf(core._t("'%s' is not a correct year"), value));
        },

        _parseClient: function (v) {
            return this._parseYearDate(v, null, {timezone: false});
        }

    });

    // Widget 'year_format' to be added from the xml at field declaration
    var YearFormatFieldDate = FieldDate.extend({
        supportedFieldTypes: ['date'],

        init: function () {
            this._super.apply(this, arguments);
            this.datepickerOptions = _.defaults(
                {},
                this.nodeOptions.datepicker || {},
                {
                    defaultDate: this.value,
                    format: this._convertYearDateFormat(time.getLangDateFormat()),
                    viewMode: 'years'  // Mostrar solo el selector de años
                }
            );
        },

        _convertYearDateFormat: function (dateFormat) {
            return "YYYY";  // Siempre solo el formato de año
        },

        _formatYearDate: function (value, field, options) {
            if (value === false) {
                return "";
            }
            return value.format(this.datepickerOptions.format);
        },

        _formatValue: function (value) {
            var options = _.extend({}, this.nodeOptions, { data: this.recordData }, this.formatOptions);
            return this._formatYearDate(value, this.field, options);
        },

        _makeDatePicker: function () {
            return new YearDateWidget(this, this.datepickerOptions);
        }

    });

    fieldRegistry.add('year_format', YearFormatFieldDate);

    return {
        YearDateWidget: YearDateWidget
    }

});
