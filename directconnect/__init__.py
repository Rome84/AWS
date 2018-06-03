
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
from boto.regioninfo import RegionInfo, get_regions
from boto.regioninfo import connect


def regions():
    """
    Get all available regions for the AWS DirectConnect service.
    :rtype: list
    :return: A list of :class:`boto.regioninfo.RegionInfo`
    """
    from boto.directconnect.layer1 import DirectConnectConnection
    return get_regions('directconnect', connection_cls=DirectConnectConnection)


def connect_to_region(region_name, **kw_params):
    from boto.directconnect.layer1 import DirectConnectConnection
    return connect('directconnect', region_name,
                   connection_cls=DirectConnectConnection, **kw_params)
