#This is a test file
import android
app = android.Android(('127.0.0.1', 8023))
app.makeToast('This is a test file\n')
a = app.environment()
app.makeToast(a)
code = app.scanBarcode()
isbn = code['result']['SCAN_RESULT']
url = 'http://books.google.com?q=%d' % isbn
droid.startActivity('android.intent.action.VIEW', url)