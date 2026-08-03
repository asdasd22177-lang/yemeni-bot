[app]

title = Essa Walkie
package.name = essawalkie
package.domain = org.essa
source.dir = .
version = 1.0

source.include_exts = py,png,jpg,kv,atlas,txt

# إضافة kivy ومكتبات أندرويد الضرورية
requirements = python3,kivy

orientation = portrait

android.permissions = INTERNET,ACCESS_NETWORK_STATE

# مواصفات إصدار أندرويد لضمان التوافق
android.api = 33
android.minapi = 21
android.ndk = 25b

# قبول الترخيص تلقائياً
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
