# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
from boto.regioninfo import get_regions
from boto.regioninfo import connect


def regions():
    """
    Get all available regions for the AWS Datapipeline service.
    :rtype: list
    :return: A list of :class:`boto.regioninfo.RegionInfo`
    """
    from boto.datapipeline.layer1 import DataPipelineConnection
    return get_regions('datapipeline', connection_cls=DataPipelineConnection)


def connect_to_region(region_name, **kw_params):
    from boto.datapipeline.layer1 import DataPipelineConnection
    return connect('datapipeline', region_name,
                   connection_cls=DataPipelineConnection, **kw_params)